return {
  {
    "kylechui/nvim-surround",
    event = "VeryLazy",
    config = function()
      require("nvim-surround").setup {
        -- Default config is fine
        -- If I change my mind, edit here
      }
    end,
  },
}
