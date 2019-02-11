I=imread('coins.png'); %Read in image
subplot(1,2,1), imshow(I); %Display image
subplot(1,2,2), imhist(I); %Display histogram

I=imread('coins.png'); %Read in image
[counts,bins]=imhist(I); %Get histogram bin values
counts(60) %Query 60th bin value