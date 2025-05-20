return {
  {
    "fedepujol/move.nvim",
    opts = {
      char = { enable = true },
    },
    lazy = false,
  },
  {
    "hedyhli/outline.nvim",
    event = "VeryLazy",
    config = function()
      vim.keymap.set("n", "<leader>o", "<cmd>Outline<CR>", { desc = "Toggle Outline" })

      require("outline").setup({
        -- Config here
      })
    end,
  },
}
