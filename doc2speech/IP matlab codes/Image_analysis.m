 B=rand(256).*1000;
imshow(B);
imagesc(B);
axis image; axis off;
colormap(gray); colorbar;
imshow(B,[0 1000]);
colormap(pink);
 colormap(gray);
B=imread('cell.tif');
C=imread('spine.tif');
D=imread('onion.tif');
 D=imread('onion.png');
subplot(3,1,1); imagesc(B); axis image
imshow(A)

imshow(B)
imshow(C)
imshow(D)
subplot(3,1,1); imagesc(B); axis image
axis off; colormap(gray);
subplot(3,1,2); imagesc(C); axis image;
axis off; colormap(jet);
subplot(3,1,3); imshow(D);
axis off; colormap(gray);

imview(B); 
B(25,50) 
 B(25,50)=255; %Set pixel value at (25,50) to white
imshow(B); %View resulting changes in image
D(25,50,:) %Print RGB pixel value at location (25,50)
D(25,50,1) %Print only the red value at (25,50)

%RGB TO GRAYSCALE IMAGE CONVERSION
D=imread('onion.png');
Dgray=rgb2gray(D);
subplot(2,1,1); imshow(D); axis image; %Display both side by side
subplot(2,1,2); imshow(Dgray);

%DIVIDING AN IMAGE INTO CHANNELS
subplot(2,1,1); imshow(D); axis image; %Display both side by side
subplot(2,1,2); imshow(Dgray);
D=imread('onion.png');
Dred=D(:,:,1);
Dgreen=D(:,:,2);
Dblue=D(:,:,3);
subplot(2,2,1); imshow(D); axis image;
subplot(2,2,2); imshow(Dred); title('red'); %Display and label
subplot(2,2,3); imshow(Dgreen); title('green');
subplot(2,2,4); imshow(Dblue); title('blue');


% ABSOLUTE DIFFERENCE BETWEEN NORMAL A GAUSSIAN FILTERED IMAGE
 I = imread('cameraman.tif');
J = uint8(filter2(fspecial('gaussian'), I));
K = imabsdiff(I,J);
figure
imshow(K,[])
imshow(J)
%END HERE

