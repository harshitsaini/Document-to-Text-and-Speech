f=ones(64,1); f=f./sum(f); %Define rectangle signal f and normalize
g=conv(f,f); g=g./sum(g); %Convolve f with itself to give g and normalize
h=conv(g,g); h=h./sum(h); %Convolve g with itself to give h and normalize
j=conv(h,h); j=j./sum(j); %Convolve h with itself to give j and normalize
subplot(2,2,1),plot(f,'k '); axis square;
axis off;
subplot(2,2,2),plot(g,'k'); axis square;
axis off;
subplot(2,2,3),plot(h,'k'); axis square;
axis off;
subplot(2,2,4),plot(j,'k'); axis square;
axis off;


%----------------------------------------------------------------------------
A=imread('onion.png'); %Read in image
PSF= fspecial('gaussian',[5 5],2); %Define Gaussian convolution kernel
h=fspecial('motion',10,45); %Define motion filter
% this mayy be used --->img= imread('cameraman.tif')
%im2double(img)
A=im2double(A)
B=conv2(PSF,rgb2gray(A)); %Convolve image with convolution kernel
C=imfilter(A,h,'replicate'); %Convolve motion PSF using alternative function
D=conv2(rgb2gray(A),rgb2gray(A)); %Self convolution motion blurred with original
subplot(2,2,1),imshow(A); %Display original image
subplot(2,2,2),imshow(B,[]); %Display filtered image
subplot(2,2,3),imshow(C,[]); %Display filtered image
subplot(2,2,4),imshow(D,[]); %Display convolution image with itself (autocorrln)