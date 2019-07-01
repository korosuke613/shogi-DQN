#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'src/script'))
	print(os.getcwd())
except:
	pass

#%%
import shogi


#%%
board = shogi.Board()
print(board.kif_str())

#%%
shogi.A1
(9-1) + 0*9

#%%
# △7六歩
usi = '7g7f'
from_usi = '7g'
from_usi_num = (9-7) + (7-1) * 9
to_usi = '7f'
to_usi_num = (9-7) + (6-1) * 9
attackers = board.attackers(shogi.BLACK, to_usi_num)
print(attackers)
if from_usi_num in attackers:
    board.push(shogi.Move.from_usi(usi))
    print(board.kif_str())
else:
    print(False)

#%%
board.is_attacked_by(shogi.WHITE, shogi.D4)

#%%
board.piece_at(shogi.D4)

#%%
# ▲3四歩
board.push_usi('3c3d')
print(board.kif_str())


#%% △2二角成
board.push_usi('8h2b+')
print(board.kif_str())


#%%
board.push_usi('4a5b')
print(board.kif_str())


#%%
board.push_usi('B*4b')
print(board.kif_str())


#%%
board.push_usi('5a4a')
print(board.kif_str())


#%%
board.push_usi('2b3a')
print(board.kif_str())


#%%
board.is_checkmate()


#%%
print(board)


#%%
print(board.kif_str())


#%%



