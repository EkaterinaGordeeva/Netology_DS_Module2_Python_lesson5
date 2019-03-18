import numpy as np
import pandas as pd

print('������� ������ �������:')
N=int(input())

#������� 1. �������� numpy array
A1=np.linspace(N-1,0,N)
print(A1)

#������� 2. �������� ������������ ������� � ���������� ����� ������������ ���������
A2 = np.diag(np.linspace(N-1, 0,N))
print(A2.sum())

#������� 3.
ratings = pd.read_csv('C:/Users/Katya/Desktop/ratings.csv')
movies = pd.read_csv('C:/Users/Katya/Desktop/movies.csv') 
#����� ������, � �������������� ����� ������=5
maxRating=ratings[ratings.rating==5].groupby('movieId').count().sort_values('rating', ascending=False).head(1)
#����������� ����������� ������� � movies ��� �������������� ������
maxRating.merge(movies, on='movieId', how='left')[['movieId', 'title']]

#������� 4.
data = pd.read_csv('C:/Users/Katya/Desktop/power.csv')

#�������� �� ��, ��� ������ ���������� � �������
data[data['country'].str.contains('atv', case=False)| data['country'].str.contains('est', case=False)|data['country'].str.contains('lit', case=False)]['country'].unique()

#����� �� ���-�� ��������� ������� � ������� � ���� data.country in [������������ ��������]? �� ���������� � ���������� �����������.
data[((data.country=='Latvia')|(data.country=='Lithuania')|(data.country=='Estonia'))&((data.category==4)|(data.category==12)|(data.category==21))&(data.year>=2005)&(data.year<=2010)&data.quantity>=0]['quantity'].sum()

#������� 5. ������ ������� ���������
#M*[x,y,z]=N, [x,y,z] = M(-1)*N
#xyz=np.array([['x'],['y'],['z']])
M=np.array([[4,2,1],[1,3,0],[0,5,4]])
N=np.array([[4],[12],[-3]])
result=M.transpose().dot(N)
for i in range(xyz.shape[0]):
	print(xyz[i],' = ', result[i])