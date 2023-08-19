import torch
import torch.nn as nn
import torch.nn.functional as F

class TransformerLayer(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout_rate):
        super(TransformerLayer, self).__init__()
        self.self_attention = nn.MultiheadAttention(hidden_size, num_heads, dropout=dropout_rate)
        self.feed_forward = nn.Sequential(
            nn.Linear(hidden_size, 4 * hidden_size),
            nn.ReLU(),
            nn.Linear(4 * hidden_size, hidden_size)
        )
        self.dropout = nn.Dropout(dropout_rate)
        self.layer_norm = nn.LayerNorm(hidden_size)

    def forward(self, inputs):
        attention_output, _ = self.self_attention(inputs, inputs, inputs)
        attention_output = self.dropout(attention_output)
        attention_output = self.layer_norm(inputs + attention_output)

        ff_output = self.feed_forward(attention_output)
        ff_output = self.dropout(ff_output)
        output = self.layer_norm(attention_output + ff_output)
        return output
class Transformer(nn.Module):
    def __init__(self, hidden_size, num_layers, num_heads, dropout_rate):
        super(Transformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.transformer_layers = nn.ModuleList([
            TransformerLayer(hidden_size, num_heads, dropout_rate) for _ in range(num_layers)
        ])

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        outputs = embeddings

        for layer in self.transformer_layers:
            outputs = layer(outputs)

        return outputs
hidden_size = 512
num_layers = 6
num_heads = 8
dropout_rate = 0.1
vocab_size = 1000

model = Transformer(hidden_size, num_layers, num_heads, dropout_rate)
inputs = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # 输入数据的形状为 [batch_size, sequence_length]
outputs = model(inputs)
print("输入是{}，输出是{}\n".format(inputs,outputs))
print("输入的shape是{}，输出的shape是{}".format(inputs.shape,outputs.shape))
