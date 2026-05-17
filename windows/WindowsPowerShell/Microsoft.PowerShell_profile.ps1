if (Test-Path alias:ls) { Remove-Item alias:ls }

function ls { & ls.exe --color=auto $args }
function la { & ls.exe --color=auto -a $args }
function ll { & ls.exe --color=auto -lh $args }
function lla { & ls.exe --color=auto -lah $args }

function nvimp { $env:NVIM_APPNAME = "nvim/nvim-custom";  nvim.exe @args }
function nvimc { $env:NVIM_APPNAME = "nvim/nvim-nvchad";  nvim.exe @args }
function nvim  { $env:NVIM_APPNAME = "nvim/nvim-lazyvim"; nvim.exe @args }
