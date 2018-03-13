A=imread('cameraman.tif'); %Read in image
subplot(1,2,1), imshow(A); %Display image
B =imadd(A, 100); %Add 100 to each pixel value in image A
subplot(1,2,2), imshow(B); %Display result image B

A=imread('cola1.png'); %Read in 1st image
B=imread('cola2.png'); %Read in 2nd image
subplot(1,3,1), imshow(A); %Display 1st image
subplot(1,3,2), imshow(B); %Display 2nd image
Output = imsubtract(A, B); %Subtract images
subplot(1,3,3), imshow(Output); %Display result

A=imread('cameraman.tif'); %Read in image
subplot(1,2,1), imshow(A); %Display image
B = imcomplement(A); %Invert the image
subplot(1,2,2), imshow(B); %Display result image B

