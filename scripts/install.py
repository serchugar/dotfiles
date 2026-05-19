import os
import platform
import shutil
from pathlib import Path


OS: str = platform.system()
REPO: Path = Path(__file__).parent.parent.resolve()
HOME: Path = Path.home()


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
    copy(REPO / "shared/git/.gitconfig", HOME / ".gitconfig")
    symlink(REPO / "shared/wezterm/.wezterm.lua", HOME / ".wezterm.lua")

    if OS == "Linux":
        CONFIG: Path = HOME / ".config"
        symlink(REPO / "shared/alacritty", CONFIG / "alacritty")

    elif OS == "Windows":
        APPDATA: Path = Path(os.environ["APPDATA"])
        symlink(REPO / "shared/alacritty", APPDATA / "alacritty")

    else:
        raise SystemExit(f"OS not supported: {OS}")
    print()
