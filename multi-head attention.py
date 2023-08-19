import math
import cv2
import torch
import torch.nn as nn

x = cv2.imread(r"C:\Users\13486\Desktop\transformer-model-architecture.jpg")
print(x.shape)

# 代码解读
class Attention(nn.Module):  # Multi-head selfAttention 模块
    def __init__(self,
                 dim,   # 输入token的dim
                 num_heads=8,  # head的个数
                 qkv_bias=False,  # 生成qkv时是否使用偏置
                 qk_scale=None,
                 attn_drop_ratio=0.,  # 两个dropout ratio
                 proj_drop_ratio=0.):
        super(Attention, self).__init__()
        self.num_heads = num_heads
        head_dim = dim // num_heads  # 每个head的dim
        self.scale = qk_scale or head_dim ** -0.5  # 不去传入qkscale，也就是1/√dim_k
        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)  # 使用一个全连接层，一次得到qkv
        self.attn_drop = nn.Dropout(attn_drop_ratio)
        self.proj = nn.Linear(dim, dim)  # 把多个head进行Concat操作，然后通过Wo映射，这里用全连接层代替
        self.proj_drop = nn.Dropout(proj_drop_ratio)
 
    def forward(self, x):
        # [batch_size, num_patches + 1, total_embed_dim] 加1代表类别，针对ViT-B/16，dim是768
        B, N, C = x.shape
 
        # qkv(): -> [batch_size, num_patches + 1, 3 * total_embed_dim]
        # reshape: -> [batch_size, num_patches + 1, 3（代表qkv）, num_heads（代表head数）, embed_dim_per_head（每个head的qkv维度）]
        # permute: -> [3, batch_size, num_heads, num_patches + 1, embed_dim_per_head]
        # permute按照数字的大小的维度存储到数字所在位置
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        # [batch_size, num_heads, num_patches + 1, embed_dim_per_head]
        q, k, v = qkv[0], qkv[1], qkv[2]  # make torchscript happy (cannot use tensor as tuple)
 
        # transpose: -> [batch_size, num_heads, embed_dim_per_head, num_patches + 1]
        # @: multiply -> [batch_size, num_heads, num_patches + 1, num_patches + 1]
        attn = (q @ k.transpose(-2, -1)) * self.scale  # 每个header的q和k相乘，除以√dim_k（相当于norm处理）
        attn = attn.softmax(dim=-1)  # 通过softmax处理（相当于对每一行的数据softmax）
        attn = self.attn_drop(attn)  # dropOut层
 
        # @: multiply -> [batch_size, num_heads, num_patches + 1, embed_dim_per_head]
        # transpose: -> [batch_size, num_patches + 1, num_heads, embed_dim_per_head]
        # reshape: -> [batch_size, num_patches + 1, total_embed_dim]
        x = (attn @ v).transpose(1, 2).reshape(B, N, C)  # 得到的结果和V矩阵相乘（加权求和），reshape相当于把head拼接
        x = self.proj(x)  # 通过全连接进行映射（相当于乘论文中的Wo）
        x = self.proj_drop(x)  # dropOut
        return x



import torch
import torch.nn as nn
import torch.nn.functional as F

class Transformer(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_heads, num_layers):
        super(Transformer, self).__init__()

        self.embedding = nn.Embedding(input_dim, hidden_dim)
        self.position_encoding = PositionalEncoding(hidden_dim)

        self.transformer_blocks = nn.ModuleList([
            TransformerBlock(hidden_dim, num_heads) 
            for _ in range(num_layers)
        ])

        self.fc = nn.Linear(hidden_dim, input_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        encoded = self.position_encoding(embedded)

        for transformer_block in self.transformer_blocks:
            encoded = transformer_block(encoded)

        logits = self.fc(encoded)
        probabilities = F.softmax(logits, dim=-1)

        return probabilities

class PositionalEncoding(nn.Module):
    def __init__(self, hidden_dim, max_length=1000):
        super(PositionalEncoding, self).__init__()

        position_encoding = torch.zeros(max_length, hidden_dim)

        position = torch.arange(0, max_length).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, hidden_dim, 2) * 
                             (-math.log(10000.0) / hidden_dim))

        position_encoding[:, 0::2] = torch.sin(position * div_term)
        position_encoding[:, 1::2] = torch.cos(position * div_term)

        self.register_buffer('position_encoding', position_encoding)

    def forward(self, x):
        seq_len = x.size(1)
        x = x + self.position_encoding[:seq_len, :]
        return x

class TransformerBlock(nn.Module):
    def __init__(self, hidden_dim, num_heads, dropout_prob=0.1):
        super(TransformerBlock, self).__init__()

        self.attention = MultiheadAttention(hidden_dim, num_heads)
        self.layer_norm1 = nn.LayerNorm(hidden_dim)
        self.feed_forward = FeedForward(hidden_dim)
        self.layer_norm2 = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout_prob)

    def forward(self, x):
        attended = self.attention(x, x, x)
        x = self.layer_norm1(x + self.dropout(attended))

        fed_forward = self.feed_forward(x)
        x = self.layer_norm2(x + self.dropout(fed_forward))

        return x

class MultiheadAttention(nn.Module):
    def __init__(self, hidden_dim, num_heads):
        super(MultiheadAttention, self).__init__()

        self.hidden_dim = hidden_dim
        self.num_heads = num_heads

        self.head_dim = hidden_dim // num_heads

        self.q_linear = nn.Linear(hidden_dim, hidden_dim)
        self.k_linear = nn.Linear(hidden_dim, hidden_dim)
        self.v_linear = nn.Linear(hidden_dim, hidden_dim)
        self.out_linear = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, query, key, value):
        batch_size = query.size(0)

        Q = self.q_linear(query).view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.k_linear(key).view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.v_linear(value).view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
                # Attention calculation
        energy = torch.matmul(Q, K.transpose(-2, -1))
        scaled_attention = energy / math.sqrt(self.head_dim)
        attention_weights = F.softmax(scaled_attention, dim=-1)
        attended_values = torch.matmul(attention_weights, V)

        # Concatenate and linear transformation
        attended_values = attended_values.transpose(1, 2).contiguous()
        concat_attended = attended_values.view(batch_size, -1, self.hidden_dim)
        output = self.out_linear(concat_attended)

        return output

class FeedForward(nn.Module):
    def __init__(self, hidden_dim, dropout_prob=0.1):
        super(FeedForward, self).__init__()

        self.fc1 = nn.Linear(hidden_dim, hidden_dim * 4)
        self.fc2 = nn.Linear(hidden_dim * 4, hidden_dim)
        self.dropout = nn.Dropout(dropout_prob)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

def main():
    model = Transformer()
    x = cv2.imread(r"C:\Users\13486\Desktop\transformer-model-architecture.jpg")
    print(x.shape)
    model(x)



if __name__ == "__main__":
    main()



# 在这个代码示例中，Transformer类是整个Transformer模型的主体，它由嵌入层（embedding layer）、位置编码层（positional encoding layer）、多个Transformer块和最后的线性层组成。forward方法描述了整个模型的前向传播过程。

# PositionalEncoding类用于生成位置编码，它使用正弦和余弦函数来为输入序列中的每个位置生成位置编码。位置编码是通过注册缓冲区（register buffer）进行存储的，以便在前向传播中重复使用。

# TransformerBlock类是Transformer模型中的基本构建块。它由多头自注意力机制（MultiheadAttention）和前馈神经网络（FeedForward）组成。forward方法描述了一个Transformer块的前向传播过程。

# MultiheadAttention类实现了多头自注意力机制，它使用线性层对查询（query）、键（key）和值（value）进行映射和变换，计算注意力权重，并将注意力权重与值进行加权求和。forward方法描述了多头自注意力机制的前向传播过程。

# FeedForward类是前馈神经网络，它由两个线性层和一个激活函数（ReLU）组成。forward方法描述了前馈神经网络的前向传播过程。

# 这个代码示例给出了Transformer模型的基本实现，但仍可能缺少某些细节和组件，如输入数据的处理、损失函数的定义、模型初始化等。具体的实现方式可能因任务的不同而有所变化。然而，这个示例提供了一个起点，可用于理解Transformer模型的基本结构和实现原理。
