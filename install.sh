#!/bin/bash

dir=~/dotfiles

#Install vimrc
mkdir -p ~/.config/nvim
ln -s $dir/vimrc ~/.vimrc
