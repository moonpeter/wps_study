#!/usr/bin/env python
# coding: utf-8

# ### [wps문제 풀기](https://github.com/WPS-12th/Python/blob/master/11.%20%ED%81%B4%EB%9E%98%EC%8A%A4_%EA%B3%BC%EC%A0%9C.ipynb)

# In[98]:


class Pokemon:
    POKEMON_LIST = []
    
    def __init__(self, name, nature):
        self.friends = []
        self.name = name
        self.nature = nature
        self.__level = 1
        Pokemon.POKEMON_LIST.append(self)
    
    @property
    def level(self):
        print(self.__level)
    
    def level_up(self):
        self.__level += 1
    
    def add_friend(self, pokemon):
        self.friends.append(pokemon)
    
    def show_friends(self):
        if len(self.friends) == 0:
            print("피카츄에게는 친구가 없습니다....")
        else:
            tmp = []
            [tmp.append(i.name) for i in self.friends ]
            print('피카츄의 친구들 : {friends} ({cnt}마리)'.format(friends=", ".join(tmp), cnt=len(tmp)))
    
    @classmethod
    def show_total_pokemon(cls):
        if len(cls.POKEMON_LIST) == 0:
            print("포켓몬이 없습니다...")
        else:
            tmp = []
            [tmp.append(i.name) for i in cls.POKEMON_LIST ]
            print('전체 포켓몬 : {friends} ({cnt}마리)'.format(friends=", ".join(tmp), cnt=len(tmp)))
    


# In[99]:


Pokemon.show_total_pokemon()


# In[100]:


pikachu = Pokemon(name='피카츄', nature='전기')
pikachu.level


# In[101]:


pikachu.level_up()
pikachu.level


# In[102]:


butterfree = Pokemon(name='버터플', nature='벌레')
starmie = Pokemon(name='아쿠스타', nature='물')
eevee = Pokemon(name='이브이', nature='노멀')
pikachu.show_friends()


# In[103]:


pikachu.add_friend(butterfree)
pikachu.add_friend(starmie)
pikachu.show_friends()


# In[104]:


Pokemon.show_total_pokemon()

