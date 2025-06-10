# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Installation and initialization
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
source "${ZINIT_HOME}/zinit.zsh"

# Theme
zinit ice depth=1; zinit light romkatv/powerlevel10k

# Plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# OMZ plugins
zinit snippet OMZP::git
zinit snippet OMZP::git

# Load completions
autoload -U compinit && compinit

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color $realpath'

# Key bindings
bindkey '^f' autosuggest-accept

# Shell integrations
eval "$(fzf --zsh)"

# Aliases
alias ls="ls --color"
alias l="exa -la --git --group-directories-first"
alias py="python"
alias rb="ruby"
alias cp="rsync -r --progress"
alias lg="lazygit"
alias sv="source venv/bin/activate"
alias bat="batcat"

alias -s pdf=firefox

export FZF_DEFAULT_OPTS=$FZF_DEFAULT_OPTS'
  --color=fg:#665c54,fg+:#282828,bg:-1,bg+:#ebdbb2
  --color=hl:#98971a,hl+:#79740e,info:#7c6f64,marker:#98971a
  --color=prompt:#79740e,spinner:#d65d0e,pointer:#9d0006,header:#076678
  --color=border:#282828,label:#ff0000,query:#504945
  --border="rounded" --border-label="" --preview-window="border-rounded" --prompt="❯ "
  --marker="*" --pointer="❯" --separator="─ " --scrollbar="│"
  --layout="reverse"'
export FZF_CTRL_T_OPTS="--preview 'bat -n --color=always {}'"

source ~/.profile

neofetch
