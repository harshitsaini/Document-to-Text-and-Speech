%EROSION%
bw = imread('text.png'); %Read in binary image
se = ones(6,1); %Define structuring element
bw_out=imerode(bw,se); %Erode image
subplot(1,2,1), imshow(bw); %Display original
subplot(1,2,2), imshow(bw_out); %Display eroded image

%DILATION%
bw = imread('text.png'); %Read in binary image
se1 = strel('square',4); %4 by 4 square
se2 = strel('line',5,45); %line, length 5, angle 45 degrees
bw_1=imdilate(bw,se1); %Dilate image
bw_2=imerode(bw,se2); %Erode image
subplot(1,2,1), imshow(bw_1); %Display dilated image
subplot(1,2,2), imshow(bw_2); %Display eroded image


length=18; tlevel=0.2; %Define SE and percent threshold level
A=imread('circuit.tif'); subplot(2,3,1), imshow(A) %Read image and display
B=im2bw(A,tlevel); subplot(2,3,2), imshow(~B); %Threshold image and display
SE=ones(3,length); bw1=imerode(~B,SE); %Erode vertical lines
subplot(2,3,3), imshow(bw1); %Display result
bw2=imerode(bw1,SE'); subplot(2,3,4), imshow(bw2); %Erode horizontal lines
bw3=imdilate(bw2,SE');bw4=imdilate(bw3,SE); %Dilate back
subplot(2,3,5), imshow(bw4); %Display
boundary=bwperim(bw4);[i,j]=find(boundary); %Superimpose boundaries
subplot(2,3,6), imshow(A); hold on; plot(j,i,'r.');


A=imread('enamel.tif'); subplot(1,3,1), imshow(A); %Read in image and display
bw=~im2bw(A,0.5); bw = imfill(bw,'holes'); %Threshold and fill in holes
subplot(1,3,2), imshow(bw); %Display resulting binary image
[L,num_0]=bwlabel(bw); %Label and count number in binary image
se=strel('disk',2); %Define structuring element,
radius=2
count =0; %Set number of erosions ¼ 0
num=num_0; %Initialise number of objects in image
while num>0 %Begin iterative erosion
count=count+1
bw=imerode(bw,se); %Erode
[L,num]=bwlabel(bw); %Count and label objects
P(count)=num_0+num; %Build discrete distribution
figure(2); imshow(bw); drawnow; %Display eroded binary image
end
figure(2); subplot(1,2,1), plot(0:count,[0 P],'ro'); %Plot Cumulative distribution
axis square;axis([0 count 0 max(P)]); %Force square axis
xlabel('Size'); ylabel('Particles removed') %Label axes
subplot(1,2,2), plot(diff([0 P]),'k'); axis square; %Plot estimated size density function

%Boundary extraction%
A=imread('circles.png'); %Read in binary image
bw=bwperim(A); %Calculate perimeter
se=strel('disk',5); bw1=imerode(A,se); %se allows thick perimeter extraction
subplot(1,3,1), imshow(A);
subplot(1,3,2), imshow(bw);
subplot(1,3,3), imshow(bw1); %Display results

%Extraction of connected components%
bw=imread('basic_shapes.png'); %Read in image
[L,num]=bwlabel(bw); %Get labelled image and number of objects
subplot(1,2,1), imagesc(bw); axis image; axis off; %Plot binary input image
colorbar('North'); subplot(1,2,2), imagesc(L); %Display labelled image
axis image; axis off; colormap(jet); colorbar('North')

%HIT OR MISS TRANSFORMATION
A=imread('text.png'); %Read in text
B=imcrop(A); %Read in target shape interactively
se1=B; se2=~B; %Define hit and miss structure elements
bw=bwhitmiss(A,se1,se2); %Perform hit miss transformation
[i,j]=find(bw==1); %Get explicit coordinates of locations
subplot(1,3,1), imshow(A); %Display image
subplot(1,3,2), imagesc(B); axis image;
axis off;
%Display target shape
subplot(1,3,3), imshow(A); hold on;
plot(j,i,'r'); %Superimpose locations on image

A=imread(Noisy_Two_Ls.png');
%CASE 1
se1=[0 0 0; 1 1 0; 0 1 0]; %SE1 defines the hits
se2=[1 1 1; 0 0 1; 0 0 1]; %SE2 defines the misses
bw=bwhitmiss(A,se1,se2); %Apply hit or miss transform
subplot(2,2,1), imshow(A,[0 1]); %Display Image
subplot(2,2,2), imshow(bw,[0 1]); %Display located pixels
%NOTE ALTERNATIVE SYNTAX
interval=[ 1 1 1; 1 1 1; 0 1 1]; %1s for hits, 1 for misses; 0s for don't care
bw=bwhitmiss(A,interval); %Apply hit or miss transform
subplot(2,2,3), imshow(bw,[0 1]); %Display located pixels
%CASE 2
interval=[0 1 1; 0 1 1; 0 0 0]; %1s for hits, 1 for misses; 0s for don't care
bw=bwhitmiss(A,interval); %Apply hit or miss transform
subplot(2,2,4), imshow(bw,[0 1]); %Display located pixels

A=imread('open_shapes.png'); %Read in image
se=strel('disk',10); bw=imopen(A,se); %Open with disk radius 10
subplot(1,3,1), imshow(A);
title('Original Image');
%Display original
subplot(1,3,2), imshow(bw);
title('Opening disk radius=10');
%Display opened image
se=strel('square',25); bw=imopen(A,se);
%Open with square side 25
subplot(1,3,3), imshow(bw);
title('Opening square side=25');
%Display opened image


mask=~imread('shakespeare.pbm'); %Read in binary text
mask=imclose(mask,ones(5)); %Close to bridge breaks in letters
se=strel('line',40,90); %Define vertical se length 40
marker=imerode(mask,se); %Erode to eliminate characters
im=imreconstruct(marker,mask); %Reconstruct image
subplot(3,1,1), imshow(~mask);
title('Original mask Image');
subplot(3,1,2), imshow(~marker);
title('marker image');
subplot(3,1,3), imshow(~im);
title('Opening by reconstruction');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                        %GRAY SCALE MORPHOLOGY%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

A=imread('cameraman.tif'); %Read in image
se=strel(ones(3)); %Define flat structuring element
Amax=imdilate(A,se); %Grey scale dilate image
Amin=imerode(A,se); %Grey scale erode image
Mgrad=Amax-Amin; %subtract the two
subplot(1,3,1), imagesc(Amax); axis image; axis off; %Display
subplot(1,3,2), imagesc(Amin); axis image; axis off;
subplot(1,3,3), imagesc(Mgrad); axis image; axis off;
colormap(gray);

I = imread('rice.png'); %Read in image
background = imopen(I,strel('disk',15)); %Opening to estimate background
I2 = imsubtract(I,background); %Subtract background
I3 = imadjust(I2); %Improve contrast
subplot(1,4,1), imshow(I);subplot(1,4,2), imshow(background);
subplot(1,4,3), imshow(I2);subplot(1,4,4), imshow(I3);

A = imread('rice.png'); %Read in unevenly illuminated image
se = strel('disk',12); %Define structuring element
Atophat = imtophat(A,se); %Apply tophat filter
subplot(1,3,1), imshow(A); %Display original
subplot(1,3,2), imshow(Atophat); %Display raw filtered image
B = imadjust(tophatFiltered); %Contrast adjust filtered image
subplot(1,3,3), imshow(B); %Display filtered and adjusted mage