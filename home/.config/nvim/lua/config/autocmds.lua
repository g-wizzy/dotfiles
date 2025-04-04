-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
-- Add any additional autocmds here

vim.api.nvim_create_autocmd({ "BufNewFile", "BufRead" }, {
  group = vim.api.nvim_create_augroup("filetype_glsl", { clear = true }),
  desc = "Change filetype to GLSL",
  callback = function()
    if vim.fn.expand("%:e") == "vert" or vim.fn.expand("%:e") == "frag" then
      vim.bo.filetype = "glsl"
    end
  end,
})

vim.api.nvim_create_autocmd({ "BufNewFile", "BufRead" }, {
  group = vim.api.nvim_create_augroup("filetype_glsl", { clear = true }),
  desc = "Auto toggle line wrap",
  callback = function()
    if vim.fn.expand("%:e") == "tex" or vim.fn.expand("%:e") == "md" then
      vim.bo.textwidth = 80
      vim.bo.wrap = true
    end
  end,
})
