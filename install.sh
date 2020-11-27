#!/bin/bash

dir=~/dotfiles

# Install vimrc
ln -s $dir/vimrc ~/.vimrc

# InstallS profile
ln -s $dir/profile ~/.profile

# Install zsh profile
ln -s $dir/zshrc ~/.zshrc

# Install kitty
mkdir -p ~/.config/kitty
ln -s $dir/kitty/kitty.conf ~/.config/kitty/kitty.conf
ln -s $dir/kitty/theme.conf ~/.config/kitty/theme.conf

# Install starship
curl -fsSL https://starship.rs/install.sh | bash
ln -s ~/dotfiles/starship.toml ~/.config/starship.toml

# Install qtile config
mkdir -p ~/.config/qtile
ln -s $dir/qtile/config.py ~/.config/qtile/config.py
ln -s $dir/qtile/hooks.py ~/.config/qtile/hooks.py
ln -s $dir/qtile/groups.py ~/.config/qtile/groups.py
ln -s $dir/qtile/keys.py ~/.config/qtile/keys.py
ln -s $dir/qtile/layouts.py ~/.config/qtile/layouts.py
ln -s $dir/qtile/screens.py ~/.config/qtile/screens.py
ln -s $dir/qtile/autostart.sh ~/.config/qtile/autostart.sh

# Install picom configuration
ln -s $dir/picom.conf ~/.config/picom.conf
