require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set
local unmap = vim.keymap.del

map("n", ";", ":", { desc = "CMD enter command mode" })
map("i", "jk", "<ESC>")

-- Telescope
unmap("n", "<leader>fa")
map(
  "n",
  "<leader> ",
  "<cmd>Telescope live_grep<CR>",
  { desc = "telescope live grep" }
)

-- tabufline
unmap("n", "<tab>")
unmap("n", "<S-tab>")

map("n", "<S-h>", function()
  require("nvchad.tabufline").prev()
end, { desc = "buffer goto prev" })
map("n", "<S-l>", function()
  require("nvchad.tabufline").next()
end, { desc = "buffer goto next" })

-- Move
map("n", "<A-j>", ":MoveLine(1)<CR>", { desc = "Move line down" })
map("n", "<A-k>", ":MoveLine(-1)<CR>", { desc = "Move line up" })
map("n", "<A-h>", ":MoveHChar(-1)<CR>", { desc = "Move char left" })
map("n", "<A-l>", ":MoveHChar(1)<CR>", { desc = "Move char right" })

-- Visual-mode commands
map("v", "<A-j>", ":MoveBlock(1)<CR>", { desc = "Move block down" })
map("v", "<A-k>", ":MoveBlock(-1)<CR>", { desc = "Move block up" })
map("v", "<A-h>", ":MoveHBlock(-1)<CR>", { desc = "Move block left" })
map("v", "<A-l>", ":MoveHBlock(1)<CR>", { desc = "Move block right" })

-- global
map("n", "<leader>qq", "<cmd>qa!<CR>", { desc = "exit nvim" })

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")
