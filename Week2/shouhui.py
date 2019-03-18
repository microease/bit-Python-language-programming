from PIL import Image
import numpy as np
a = np.asarray(Image.open('avatar.png').convert('L')).astype('float')
depth = 10. 						#深度值 (0-100)
grad = np.gradient(a)				#取图像灰度的梯度值
grad_x, grad_y = grad 				#分别取横纵图像梯度值
grad_x = grad_x*depth/100.          #根据深度值调整横纵方向的梯度值
grad_y = grad_y*depth/100.
#梯度归一化
A = np.sqrt(grad_x**2 + grad_y**2 + 1.) 
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
#光源归一化
vec_el = np.pi/2.2 					#光源的俯视角度，弧度值
vec_az = np.pi/4. 					#光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az) 	#光源对x轴的影响
dy = np.cos(vec_el)*np.sin(vec_az) 	#光源对y轴的影响
dz = np.sin(vec_el) 				#光源对z轴的影响
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z) 	#梯度与光源相互作用，将梯度转换为灰度
b = b.clip(0,255)							#防止数据越界，将生成的灰度值裁剪至0-255
im = Image.fromarray(b.astype('uint8')) 	#重构图像
im.save('avatar1.jpg')