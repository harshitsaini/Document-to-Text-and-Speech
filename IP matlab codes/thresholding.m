I=imread('trees.tif'); %Read in 1st image
T=im2bw(I, 0.1); %Perform thresholding
subplot(1,3,1), imshow(I); %Display original image
subplot(1,3,2), imshow(T); %Display thresholded image