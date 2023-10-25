#!/bin/bash

dir=~/.dotfiles
mkdir -p ~/.config

# Configure vimrc
ln -s $dir/vimrc ~/.vimrc

# Configure ranger
ln -s $dir/ranger ~/.config/ranger

# Configure profile
ln -s $dir/profile ~/.profile

# Configure zsh profile
ln -s $dir/zshrc ~/.zshrc

# Configure kitty
ln -s $dir/kitty ~/.config/

# Configure qtile config
ln -s $dir/qtile ~/.config/

# Configure picom
ln -s $dir/picom.conf ~/.config/picom.conf

# Configure rofi
ln -s $dir/rofi ~/.config/

# Configure vscode
mkdir -p ~/.config/Code\ -\ OSS/User
ln -s $dir/vscodium-settings.json "$HOME/.config/Code - OSS/User/settings.json"

# Configure custom scripts
ln -s $dir/scripts $HOME

