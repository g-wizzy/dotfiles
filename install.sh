#!/bin/bash

dir=~/dotfiles

#Install vimrc
ln -s $dir/vimrc ~/.vimrc

#Install bash profile
ln -s $dir/profile ~/.profile
# TODO: add zshrc