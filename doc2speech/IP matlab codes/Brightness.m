A=input('brightness factor?');
B=imread('cameraman.jpg');
[x,y]=size(B);
for i=1:1:x
    for j=1:1:y
        C(i,j)=B(i,j)+A;
    end
end
subplot(1,2,1), subimage(B),title('Before');
subplot(1,2,2), subimage(C),title('After'),
xlabel(sprintf('Brightness increased by a factor of %g',A));
