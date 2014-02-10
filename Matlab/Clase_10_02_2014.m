clear all
close all
clc
%% se declaran las clases %%
clase1 = [1 3 1 2 3;2 5 5 2 3];
clase2 = [6 6 7 8 8;4 3 4 4 5];
vector = [4;5];
%% se obtienen las medias de las clases %%
media1 = mean(clase1');
media2 = mean(clase2');
%% se realiza la resta (x - u) para la clase 1%%
auxClase1_1 = clase1(1,:)-media1(:,1);
auxClase1_2 = clase1(2,:)-media1(:,2);
%% se realiza la resta (x - u) para la clase 2%%
auxClase2_1 = clase2(1,:)-media2(:,1);
auxClase2_2 = clase2(2,:)-media2(:,2);
%% se guarda el resultado de la clase 1 en una matriz %%
totalRestaClase1 = [auxClase1_1;auxClase1_2];
%% se guarda el resultado de la clase 2 en una matriz %%
totalRestaClase2 = [auxClase2_1;auxClase2_2];
%% se calcula la matriz de Varianza para la clase 1 %%
matrizVarianza1 = 1/5*totalRestaClase1*(totalRestaClase1)';
matrizVarianza2 = 1/5*totalRestaClase2*(totalRestaClase2)';
%% se obtienen las inversas de las matrices de varianza %%
inversaMatrizVarianza1 = inv(matrizVarianza1);
inversaMatrizVarianza2 = inv(matrizVarianza2);
%% se obtiene la resta del vector deseado menos la media %%
%% clase 1 %%
aux_VectorMedia1_1 = vector(1,:) - media1(:,1);
aux_VectorMedia1_2 = vector(2,:) - media1(:,2);
%% clase 2 %%
aux_VectorMedia2_1 = vector(1,:) - media2(:,1);
aux_VectorMedia2_2 = vector(2,:) - media2(:,2);
%% se almacenan las restas en el vector 
vectorResta1 = [aux_VectorMedia1_1;aux_VectorMedia1_2];
vectorResta2 = [aux_VectorMedia2_1;aux_VectorMedia2_2];
%% se calcula la pertenencia mediante la distancia de Mahalanobis %%
distancia1 = (vectorResta1')*inversaMatrizVarianza1*(vectorResta1)
distancia2 = (vectorResta2')*inversaMatrizVarianza2*(vectorResta2)
disp('ok')