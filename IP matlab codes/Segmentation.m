I = imread('coins.png'); %Read in original
subplot(2,2,1), imshow(I); %Display original
subplot(2,2,2),im2bw(I,0.35); %Result of manual threshold
[counts,X]=imhist(I); %Calculate image hIstogram
P = polyfit(X,counts,6); Y=polyval(P,X); %Fit to histogram and evaluate
[V,ind]=sort(abs(diff(Y))); thresh=ind(3)./255; %Find minimum of polynomial
subplot(2,2,3), im2bw(I,thresh); %Result of Polynomial theshold
level = graythresh(I); %Find threshold
subplot(2,2,4), im2bw(I,level); %Result of Otsu's method
figure; plot(X,counts); hold on, plot(X,Y,'r'); %Histogram and polynomial fit

%%%%%%SPLIT AND MERGE ALGORITHM%%%%%%
I=imread('cameraman.tif'); %Read in image
S = qtdecomp(I,.17); %Do quadtree decomposition
blocks = repmat(uint8(0),size(S)); %Create empty blocks
for dim = [512 256 128 64 32 16 8 4 2 1]; %Loop through successively smaller blocks
numblocks = length(find(S==dim));
if (numblocks > 0)
values = repmat(uint8(1),[dim dim numblocks]);
values(2:dim,2:dim,:) = 0;
blocks = qtsetblk(blocks,S,dim,values);
end
end
blocks(end,1:end) =1;
blocks(1:end,end) = 1;
subplot(1,2,1), imshow(I);
k=find(blocks==1); %Find border pixels of regions
A=I; A(k)=255; %Superimpose on original image
subplot(1,2,2), imshow(A);

%%%%%%%%%%%%CANNY EDGE DETECTION%%%%%%%%%%%%%%%
A=imread('cameraman.tif'); %Read in image
subplot(3,3,1), imshow(A,[]); %Display original
h1=fspecial('gaussian',[15 15],6);
h2=fspecial('gaussian',[30 30],12);
subplot(3,3,4), imshow(imfilter(A,h1),[]); %Display filtered version sigma¼6
subplot(3,3,7), imshow(imfilter(A,h2),[]); %Display filtered version sigma¼12
[bw,thresh]=edge(A,'log'); %Edge detection on original LoG filter
subplot(3,3,2), imshow(bw,[]);
[bw,thresh]=edge(A,'canny'); %Canny edge detection on original
subplot(3,3,3), imshow(bw,[]); %Display
[bw,thresh]=edge(imfilter(A,h1),'log'); %LoG edge detection on sigma=6
subplot(3,3,5), imshow(bw,[]);
[bw,thresh]=edge(imfilter(A,h1),'canny'); %Canny edge detection on sigma=6
subplot(3,3,6), imshow(bw,[]);
[bw,thresh]=edge(imfilter(A,h2),'log'); %LoG edge detection on sigma=12
subplot(3,3,8), imshow(bw,[]);
[bw,thresh]=edge(imfilter(A,h2),'canny'); %Canny edge detection on sigma=12
subplot(3,3,9), imshow(bw,[]);

%%%%%%%%%WATER SHED SEGMENTATION%%%%%%%%%%%%%%%
center1 = 10; %Create image comprising two perfectly
center2 = center1; %smooth overlapping circles
dist = sqrt(2*(2*center1)^2);
radius = dist/2 * 1.4;
lims = [floor(center1+1.2*radius)+ceil(center2+1.2*radius)];
[x,y] = meshgrid(lims(1):lims(2));
bw1 = sqrt((x+center1).^2+ (y+center1).^2) <= radius;
bw2 = sqrt((x+center2).^2+ (y+center2).^2) <= radius;
bw = bw1 | bw2;
D = bwdist(~bw); %Calculate basic segmentation function
%(Euclidean distance transform
%of bw)
subplot(2,2,1), imshow(bw,[]); %Display image
subplot(2,2,2), imshow(D,[]); %Display basic segmentation function
%Modify segmentation function
D = ~D; %Invert and set background pixels
%lower
D(~bw) = inf; %than all catchment basin minima
subplot(2,2,3), imshow(D,[]); %Display modified segmentation image
L = watershed(D); subplot(2,2,4), Imagesc(L); %Calculate watershed of segmentation
%function
axis image; axis off; colormap(hot); colorbar %Display labelled image colour
%coded
A=imread('overlapping euros1.png'); %Read in image
bw=im2bw(A,graythresh(A)); %Threshold automatically
se=strel('disk',10); bwo=imopen(bw,se); %Remove background by opening
D = bwdist(~bwo); %Calculate basic segmentation function
D = ~D; D(~bwo) = 255; %Invert, set background lower than
%catchment basin minima
L = watershed(D); %Calculate watershed
subplot(1,4,1), imshow(A); %Display original
subplot(1,4,2), imshow(bw) %Thresholded image
subplot(1,4,3), imshow(D,[]); %Display basic segmentation function
ind=find(L==0); Ac=A; Ac(ind)=0; %Identify watersheds and set¼0 on original
subplot(1,4,4), Imagesc(Ac); hold on %Segmentation superimposed on original
Lrgb = label2rgb(L,'jet', 'w', 'shuffle'); %Calculate label image
himage = imshow(Lrgb); set(himage,'AlphaData', 0.3);
