-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local map = vim.keymap.set

map("i", "jk", "<ESC>")

---------------------------------
-- MOVE -------------------------
---------------------------------
map("n", "<A-j>", ":MoveLine(1)<CR>", { desc = "Move line down" })
map("n", "<A-k>", ":MoveLine(-1)<CR>", { desc = "Move line up" })
map("n", "<A-h>", ":MoveChar(-1)<CR>", { desc = "Move char left" })
map("n", "<A-l>", ":MoveChar(1)<CR>", { desc = "Move char right" })

map("v", "<A-j>", ":MoveBlock(1)<CR>", { desc = "Move block down" })
map("v", "<A-k>", ":MoveBlock(-1)<CR>", { desc = "Move block up" })
map("v", "<A-h>", ":MoveHBlock(-1)<CR>", { desc = "Move block left" })
map("v", "<A-l>", ":MoveHBlock(1)<CR>", { desc = "Move block right" })

---------------------------------
-- TERMINAL ---------------------
---------------------------------
map("n", "<leader>t", "<cmd>ToggleTerm<CR>", { desc = "Toggle terminal window" })
map("t", "<C-x>", "<C-\\><C-N>", { desc = "terminal escape terminal mode" })
