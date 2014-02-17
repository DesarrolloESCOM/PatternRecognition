clear all
close all
clc
%% Clases %%
C1 = [4 5 4 3 5; 3 4 4 4 3];
C2 = [ 7 7 6 5.8 9; 4 5 4 4.9 5 ];
C3 = [ 7 6 6 7 8; 7 7 6 6 7 ];
%% vector representante %%
x = [5.1 4.1];
%% vector de distancias %%
vectorDistanciasC1= [];
vectorDistanciasC2= [];
vectorDistanciasC3= [];
%% Se obtiene la media %%
mediaClase1 = mean(C1');
mediaClase2 = mean(C2');
mediaClase3 = mean(C3');
%% se obtienen las distancias usando el metodo euclidiano %%
%% todo este proceso se puede realizar de manera iteraiva, se cambiará en python
%% distancias con la clase 1 %%
vectorDistanciasC1(1) = sqrt((C1(1,1) - x(1))^2 + (C1(2,1) - x(2))^2);
vectorDistanciasC1(2) = sqrt((C1(1,2) - x(1))^2 + (C1(2,2) - x(2))^2);
vectorDistanciasC1(3) = sqrt((C1(1,3) - x(1))^2 + (C1(2,3) - x(2))^2);
vectorDistanciasC1(4) = sqrt((C1(1,4) - x(1))^2 + (C1(2,4) - x(2))^2);
vectorDistanciasC1(5) = sqrt((C1(1,5) - x(1))^2 + (C1(2,5) - x(2))^2);
%% distancias con la clase 2 %%
vectorDistanciasC2(1) = sqrt((C2(1,1) - x(1))^2 + (C2(2,1) - x(2))^2);
vectorDistanciasC2(2) = sqrt((C2(1,2) - x(1))^2 + (C2(2,2) - x(2))^2);
vectorDistanciasC2(3) = sqrt((C2(1,3) - x(1))^2 + (C2(2,3) - x(2))^2);
vectorDistanciasC2(4) = sqrt((C2(1,4) - x(1))^2 + (C2(2,4) - x(2))^2);
vectorDistanciasC2(5) = sqrt((C2(1,5) - x(1))^2 + (C2(2,5) - x(2))^2);
%% distancias con la clase 3 %%
vectorDistanciasC3(1) = sqrt((C3(1,1) - x(1))^2 + (C3(2,1) - x(2))^2);
vectorDistanciasC3(2) = sqrt((C3(1,2) - x(1))^2 + (C3(2,2) - x(2))^2);
vectorDistanciasC3(3) = sqrt((C3(1,3) - x(1))^2 + (C3(2,3) - x(2))^2);
vectorDistanciasC3(4) = sqrt((C3(1,4) - x(1))^2 + (C3(2,4) - x(2))^2);
vectorDistanciasC3(5) = sqrt((C3(1,5) - x(1))^2 + (C3(2,5) - x(2))^2);
%% se ordenan los resultados %%
vectorDistanciasC1;
vectorDistanciasC2;
clase1 = sort(vectorDistanciasC1)
clase2 = sort(vectorDistanciasC2)
clase3 = sort(vectorDistanciasC3);