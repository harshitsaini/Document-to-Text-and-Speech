%------------OTSU THESHOLDING-----------%
I=imread('coins.png'); %Read in image
level=graythresh(I); %Get OTSU threshold
It=im2bw(I, level); %Threshold image
imshow(It); %Display it

%-----------ADAPTIVE THRESHOLDING-------%
I=imread('rice.png'); %Read in image
Im=imfilter(I,fspecial('average',[1 1]),'replicate'); %Create mean image
It=I+(Im-20); %Subtract mean image(þ constant C¼20)
Ibw=im2bw(It,0.0); %Threshold result at 0 (keep þve results only)
subplot(1,2,1), imshow(I); %Display image
subplot(1,2,2), imshow(It); %Display result


%----------CONTRAST STRETCHING---------%
I=imread('pout.tif'); %Read in image
Ics=imadjust(I,stretchlim(I, [0.05 0.95]),[]); %Stretch contrast using method 1
subplot(2,2,1), imshow(I); %Display image
subplot(2,2,2), imshow(Ics); %Display result

subplot(2,2,3), imhist(I); %Display input histogram
subplot(2,2,4), imhist(Ics); %Display output histogram

%----------HISTOGRAM EQUALIZATION--------%
I=imread('pout.tif'); %Read in image
Ieq=histeq(I);
subplot(2,2,1), imshow(I); %Display image
subplot(2,2,2), imshow(Ieq); %Display result
subplot(2,2,3), imhist(I); %Display histogram of image
subplot(2,2,4), imhist(Ieq); %Display histogram of result

%-----------HISTOGRAM MATCHING-----------%
I=imread('pout.tif');
pz=0:255; %Define ramp like pdf as desired output histogram
Im=histeq(I, pz); %Supply desired histogram to perform matching
subplot(2,3,1), imshow(I); %Display image
subplot(2,3,2), imshow(Im); %Display result
subplot(2,3,3), plot(pz); %Display distribution t
subplot(2,3,4), imhist(I); %Display histogram of image
subplot(2,3,5), imhist(Im); %Display histogram of result