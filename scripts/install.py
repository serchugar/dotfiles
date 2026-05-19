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


def symlink(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        print(f"\tskipping {dst} (already exists)")
        return
    dst.symlink_to(src)
    print(f"\tlinked {dst} to {src}")


def copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        print(f"\tskipping {dst} (already exists)")
        return
    shutil.copy2(src, dst)
    print(f"\tcopied {src} into {dst}")


if __name__ == "__main__":
    print()
    copy(SHARED / "git/.gitconfig", HOME / ".gitconfig")
    symlink(SHARED / "wezterm/.wezterm.lua", HOME / ".wezterm.lua")

    if OS == "Linux":
        CONFIG: Path = HOME / ".config"
        symlink(SHARED / "alacritty", CONFIG / "alacritty")
        symlink(SHARED / "yazi", CONFIG / "yazi")

    elif OS == "Windows":
        APPDATA: Path = Path(os.environ["APPDATA"])
        symlink(SHARED / "alacritty", APPDATA / "alacritty")
        symlink(SHARED / "yazi", APPDATA / "yazi/config")

    else:
        raise SystemExit(f"OS not supported: {OS}")
    print("\nThe following programs must be installed manually:\n")
    print(
        "\t- Clangd: Copy '.clang-format' and '.clangd' files into the highest "
        "possible directory within the disk where you are storing your projects"
    )
    print(
        "\t- Powershell: open $PROFILE within a powershell session with your editor "
        "(E.g: 'nvim $PROFILE') and copy the contents of 'Microsoft.PowerShell_profile.ps1'"
    )
    print()
