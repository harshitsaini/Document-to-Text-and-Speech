A=imread('coins_and_keys.png');
subplot(1,2,1), imshow(A);
%Read in image and display
bw=~im2bw(rgb2gray(A),0.35); bw=imfill(bw,'holes'); %Threshold and fill in holes
bw=imopen(bw,ones(5)); subplot(1,2,2), imshow(bw,[0 1]); %Morphological opening
[L,num]=bwlabel(bw); %Create labelled image
s=regionprops(L,'area','perimeter'); %Calculate region properties
for i=1:num %Object's area and perimeter
x(i)=s(i).Area;
y(i)=s(i).Perimeter;
form(i)=4.*pi.*x(i)./(y(i).^2); %Calculate form factor
end
figure; plot(x./max(x),form,'ro'); %Plot area against form factor


%%%%%%%%%%%%%%%%%HU MOMENTS%%%%%%%%%%%%

A=rgb2gray(imread('spanners.png')); %Read in image, convert to grey
bwin=~im2bw(A,0.5); %Threshold and display
[L, num]=bwlabel(bwin); %Create labelled image
subplot (2,2,1), imshow(A); %Display input image
for i=1:num %Loop through each labelled object
I=zeros(size(A)); %array for ith object
ind=find(L==i); I(ind)=1; %Find pixels belonging to ith object and set=1
subplot(2, 2, i+1), imshow(I); %Display identified object
%I=double(bw)./(sum(sum(bw)));
[rows,cols]=size(I); x=1:cols;y=1:rows; %get indices
[X,Y]=meshgrid(x,y); %Set up grid for calculation
%calculate required ordinary moments
M_00=sum(sum(I));
M_10=sum(sum(X.*I)); M 01=sum(sum(Y.*I));
xav=M_10./M_00; yav=M_01./M_00;
X=X-xav; Y=Y-yav; %mean subtract the X and Y coordinates
hold on; plot(M_10,M_01,'ko'); drawnow
%calculate required central moments
M_11=sum(sum(X.*Y.*I));
M_20=sum(sum(X.^2.*I)); M_02=sum(sum(Y.^2.*I));
M_21=sum(sum(X.^2.*Y.*I)); M_12=sum(sum(X.*Y.^2.*I));
M_30=sum(sum(X.^3.*I)); M_03=sum(sum(Y.^3.*I));
%calculate normalised central moments
eta_11=M_11./M_00.^2;
eta_20=M_20./M_00.^2;
eta_02=M_02./M_00.^2;
eta_21=M_21./M_00.^(5./2);
eta_12=M_12./M_00.^(5./2);
eta_30=M_30./M_00.^(5./2);
eta_03=M_02./M_00.^(5./2);
%calculate Hu moments
Hu_1=eta_20 + eta_02;
Hu_2=(eta_20+eta_02).^2 + (2.*eta_11).^2;
Hu_3=(eta_30+3.*eta_12).^2 + (3.*eta_21+eta_03).^2;
s=sprintf('Object number is %d', i)
s=sprintf('Hu invariant moments are %f %f %f ',Hu 1,Hu 2,Hu 3)
pause;
end

%Statistical Measures and Textures%
A=imread('sunandsea.jpg') ; %Read image
I=rgb2gray(A); %Convert to grey scale
J = stdfilt(I); %Apply local standard deviaton filter
subplot(1,4,1), imshow(I);
subplot(1,4,2),imshow(J,[]); %Display original and processed
J = entropyfilt(I,ones(15)); %Apply entropy filter over 15x15 neighbourhood
subplot(1,4,3),imshow(J,[]); %Display processed result
J = rangefilt(I,ones(5)); %Apply range filter over 5x5 neighbourhood
subplot(1,4,4),imshow(J,[]);

