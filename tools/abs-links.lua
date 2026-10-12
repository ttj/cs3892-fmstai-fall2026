-- Rewrite repository-relative links to absolute GitHub URLs.
--
-- The markdown in this repository links from one document to another with
-- relative paths (`../labs/running-example.md`), which is right on GitHub. In a
-- PDF made from that markdown the same link becomes `file:///...` on whatever
-- machine built it, and is dead for everyone else. This filter turns each
-- relative link into the document's address in this repository, so a PDF posted
-- to Brightspace links to something a student can open.
--
--   pandoc ... --lua-filter tools/abs-links.lua -M srcdir=assignments
--
-- `srcdir` is the directory of the markdown file, relative to the repository
-- root. Links that already have a scheme (https:, mailto:), and links within
-- the page (#section), are left alone. Images are not links and are untouched.

local repo = "https://github.com/ttj/cs3892-fmstai-fall2026"
local branch = "main"
local srcdir = ""

local function normalize(path)
  local out = {}
  for part in path:gmatch("[^/]+") do
    if part == ".." then
      table.remove(out)
    elseif part ~= "." then
      table.insert(out, part)
    end
  end
  return table.concat(out, "/")
end

local function read_meta(meta)
  if meta.srcdir then srcdir = pandoc.utils.stringify(meta.srcdir) end
  if meta.repo_url then repo = pandoc.utils.stringify(meta.repo_url) end
end

local function absolute(el)
  local target = el.target
  if target:match("^%a[%w+.-]*:") or target:match("^#") or target:match("^//") then
    return nil
  end
  local path, fragment = target:match("^([^#]*)(.*)$")
  local full = normalize((srcdir ~= "" and (srcdir .. "/") or "") .. path)
  local is_dir = path:match("/$") or not full:match("%.[%w]+$")
  el.target = repo .. "/" .. (is_dir and "tree" or "blob") .. "/" .. branch .. "/" .. full .. fragment
  return el
end

return { { Meta = read_meta }, { Link = absolute } }
