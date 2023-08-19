import torch
import torchvision
from torchvision import datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as Data
import matplotlib.pyplot as plt
import torchsummary
from torchsummary import summary
import netron
import onnx
from onnx import shape_inference
from backbones import ResNet,Basicblock


# define hyper parameters
Batch_size = 50
Lr = 0.1
Epoch = 1
# define train set and test set
train_dataset = torchvision.datasets.MNIST(
    root='./MNIST',
    train=True,
    download=True,
    transform=torchvision.transforms.ToTensor()
)
test_dataset = torchvision.datasets.MNIST(
    root='./MNIST',
    train=False,
    download=True,
    transform=torchvision.transforms.ToTensor()
)
# define train loader
train_loader = Data.DataLoader(
    dataset=train_dataset,
    shuffle=True,
    batch_size=Batch_size
)
test_x = torch.unsqueeze(test_dataset.data, dim=1).type(torch.Tensor)
test_y = test_dataset.targets
print(test_y.shape, test_x.shape)

ResNet18 = ResNet(Basicblock, [1, 1, 1, 1], 10)
print(ResNet18)
print("==========================================================")
# summary(ResNet18,(1,28,28),device='cpu')

# img = torch.rand((1, 1, 28, 28))
# torch.onnx.export(model=ResNet18, args=img, f='model.onnx', input_names=['image'], output_names=['feature_map'])
# onnx.save(onnx.shape_inference.infer_shapes(onnx.load("model.onnx")), "model.onnx")
# netron.start("model.onnx")

opt = torch.optim.SGD(ResNet18.parameters(), lr=Lr)
loss_fun = nn.CrossEntropyLoss()
a = []
ac_list = []
for epoch in range(Epoch):
    for i, (x, y) in enumerate(train_loader):
        output = ResNet18(x)
        loss = loss_fun(output, y)
        opt.zero_grad()
        loss.backward()
        opt.step()

        if i % 100 == 0:
            a.append(i)
            test_output = torch.max(ResNet18(test_x), dim=1)[1]
            loss = loss_fun(ResNet18(test_x), test_y).item()
            accuracy = torch.sum(torch.eq(test_y, test_output)).item() / test_y.numpy().size
            ac_list.append(accuracy)
            print('Epoch:', Epoch, '|loss%.4f' % loss, '|accuracy%.4f' % accuracy)

        model_state = {
            'state_dict': ResNet18.state_dict(),
            'optimizer': opt.state_dict(),
            'epoch': epoch,
            'loss': loss,
            }
        torch.save(model_state,"./net.pth")

print('real value', test_y[: 10].numpy())
print('train value', torch.max(ResNet18(test_x)[: 10], dim=1)[1].numpy())

plt.plot(a, ac_list, color='r')
plt.show()