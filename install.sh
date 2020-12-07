#!/bin/bash

dir=~/dotfiles

# Install vimrc
ln -s $dir/vimrc ~/.vimrc

# InstallS profile
ln -s $dir/profile ~/.profile

# Install zsh profile
ln -s $dir/zshrc ~/.zshrc

# Install kitty
ln -s $dir/kitty ~/.config/kitty

# Install starship
ln -s ~/dotfiles/starship.toml ~/.config/starship.toml

# Install qtile config
ln -s $dir/qtile ~/.config/qtile

# Install picom configuration
ln -s $dir/picom.conf ~/.config/picom.conf

# Install rofi
ln -s $dir/rofi ~/.config/rofi
