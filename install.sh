#!/bin/bash

dir=~/dotfiles

#Install vimrc
ln -s $dir/vimrc ~/.vimrc

#Install bash profile
ln -s $dir/profile ~/.profile

#Install zsh profile
ln -s $dir/zshrc ~/.zshrc

#Install qtile config
mkdir -p ~/.config/qtile
ln -s $dir/qtile/config.py ~/.config/qtile/config.py
ln -s $dir/qtile/autostart.sh ~/.config/qtile/autostart.sh

#Install compton configuration
ln -s $dir/compton.conf ~/.config/compton.conf
