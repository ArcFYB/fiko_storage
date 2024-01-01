import cv2
import os
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import structural_similarity as compare_ssim
from tqdm import tqdm  # 引入tqdm库来显示进度条

# 设定两个文件夹的路径
ref_folder = '/home/fiko/Code/DATASET/Super_resolution_data/sr-pair-val_32_128/hr_128'
test_folder = '/home/fiko/Code/Real-ESRGAN/experiments/result_PNG'

# 获取两个文件夹中的图像文件名
ref_images = os.listdir(ref_folder)
test_images = os.listdir(test_folder)

# 过滤出前十个字符相同的文件名
matched_images = [(ref, test) for ref in ref_images for test in test_images if ref[:10] == test[:10]]

# 初始化PSNR和SSIM列表
psnrs = []
ssims = []

# 遍历匹配的图像文件
for ref_image, test_image in tqdm(matched_images, unit="pair", desc="Computing PSNR and SSIM"):
    # 读取参考图像和测试图像
    ref_img = cv2.imread(os.path.join(ref_folder, ref_image), cv2.IMREAD_UNCHANGED)
    test_img = cv2.imread(os.path.join(test_folder, test_image), cv2.IMREAD_UNCHANGED)

    # 检查图像是否正确加载
    if ref_img is None or test_img is None:
        raise ValueError(f"Error loading images {ref_image} or {test_image}")
    
    # 检查图像是否有相同的维度
    if ref_img.shape != test_img.shape:
        raise ValueError(f"Error: Images {ref_image} and {test_image} have different dimensions.")
    
    # 如果图像有四个通道（比如带有alpha通道的RGBA），则去除alpha通道
    if ref_img.shape[-1] == 4:
        ref_img = ref_img[..., :3]
        test_img = test_img[..., :3]
    
    # 确保图像尺寸一致
    if ref_img.shape != test_img.shape:
        raise ValueError(f"Image sizes do not match for {ref_image} and {test_image}.")

    # 计算PSNR
    psnr_value = compare_psnr(ref_img, test_img, data_range=255)
    psnrs.append(psnr_value)
    
    # 计算SSIM，对彩色图像设置multichannel=True
    ssim_value = compare_ssim(ref_img, test_img, multichannel=True, win_size=7, channel_axis=-1)
    ssims.append(ssim_value)

# 输出平均PSNR和SSIM
average_psnr = np.mean(psnrs)
average_ssim = np.mean(ssims)

print(f'Average PSNR: {average_psnr}')
print(f'Average SSIM: {average_ssim}')



