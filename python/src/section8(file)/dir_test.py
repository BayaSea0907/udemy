import os

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir1')

os.mkdir(root,'test_dir1')

# 存在しないものはできない
# os.mkdir('test_dir2/test_dir2')
