return {
  {
    "nvim-tree/nvim-tree.lua",
    config = function()
      local function my_on_attach(bufnr)
        local api = require "nvim-tree.api"

        local function opts(desc)
          return {
            desc = "nvim-tree: " .. desc,
            buffer = bufnr,
            noremap = true,
            silent = true,
            nowait = true
          }
        end

        local function collapse_if_dir()
          local node = api.tree.get_node_under_cursor()

          if node.nodes ~= nil then
            -- expand or collapse folder
            api.node.open.edit()
          else
            -- open file
            api.node.open.edit()
          end
        end

        -- default mappings
        api.config.mappings.default_on_attach(bufnr)

        -- custom mappings
        vim.keymap.set("n", "l", api.node.open.edit, opts("Open"))
        vim.keymap.set("n", "h", api.node.navigate.parent_close, opts("Exit folder"))
        vim.keymap.set("n", "?", api.tree.toggle_help, opts("Help"))
      end
      require("nvim-tree").setup {
        on_attach = my_on_attach,
      }
    end
  }
}
