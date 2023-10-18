#!/bin/bash

dir=~/dotfiles
mkdir -p ~/.config

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

# Install .Xresources (fix cursor size)
ln -s $dir/Xresources ~/.Xresources

# Install picom configuration
ln -s $dir/picom.conf ~/.config/picom.conf

# Configure rofi
ln -s $dir/rofi ~/.config/


# Install vscode
mkdir -p "~/.config/Code - OSS/User"
ln -s $dir/settings.json "~/.config/Code - OSS/User/settings.json"

# Install custom scripts
ln -s $dir/scripts ~/scripts

