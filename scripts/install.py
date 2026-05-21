import os
import platform
import shutil
from pathlib import Path


OS: str = platform.system()
REPO: Path = Path(__file__).parent.parent.resolve()
HOME: Path = Path.home()

SHARED: Path = REPO / "shared"
LINUX: Path = REPO / "linux"
WINDOWS: Path = REPO / "windows"


def symlink(src: Path, dst: Path, name: str | None = None) -> None:
    name = name if name else (src.name if src.is_dir() else src.parent.name)
    name = name.capitalize() + ":"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        print(f"\t{name:20} skipping {dst} (already exists)")
        return
    dst.symlink_to(src)
    print(f"\t{name:20} linked {dst} to {src}")


def copy(src: Path, dst: Path, name: str | None = None) -> None:
    name = name if name else (src.name if src.is_dir() else src.parent.name)
    name = name.capitalize() + ":"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        print(f"\t{name:20} skipping {dst} (already exists)")
        return
    shutil.copy2(src, dst)
    print(f"\t{name:20} copied {src} into {dst}")


if __name__ == "__main__":
    print()
    copy(SHARED / "git/.gitconfig", HOME / ".gitconfig")
    symlink(SHARED / "wezterm/.wezterm.lua", HOME / ".wezterm.lua")

    if OS == "Linux":
        CONFIG: Path = HOME / ".config"

        symlink(SHARED / "alacritty", CONFIG / "alacritty")
        symlink(SHARED / "yazi", CONFIG / "yazi")
        symlink(SHARED / "ruff", CONFIG / "ruff")
        symlink(SHARED / "clangd", CONFIG / "clangd")

    elif OS == "Windows":
        APPDATA: Path = Path(os.environ["APPDATA"])
        LOCALAPPDATA: Path = Path(os.environ["LOCALAPPDATA"])

        symlink(SHARED / "alacritty", APPDATA / "alacritty")
        symlink(SHARED / "yazi", APPDATA / "yazi/config")
        symlink(SHARED / "ruff", APPDATA / "ruff")

        symlink(SHARED / "clangd", LOCALAPPDATA / "clangd")

    else:
        raise SystemExit(f"OS not supported: {OS}")
    print("\n\tThe following programs must be installed manually:")

    print(
        "\tPowershell: open $PROFILE within a powershell session with your editor "
        "(E.g: 'nvim $PROFILE') and copy the contents of 'Microsoft.PowerShell_profile.ps1'"
    )
    print()
