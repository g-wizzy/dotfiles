require "nvchad.options"

-- add yours here!

-- local o = vim.o
-- o.cursorlineopt ='both' -- to enable cursorline!

vim.filetype.add({
  extension = {
    vert = "glsl",
    frag = "glsl",
  },
})

vim.opt.wrap = true
vim.opt.colorcolumn = "81"
vim.wo.relativenumber = true

vim.o.title = true
vim.o.cursorlineopt = "both"
