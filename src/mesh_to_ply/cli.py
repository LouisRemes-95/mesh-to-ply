import argparse
from pathlib import Path
from rich.console import Console

from mesh_to_ply.convert import convert

def main():
    parser = argparse.ArgumentParser(
        prog = ".mesh to .ply", 
        description = "Convert a .mesh (or other meshio-supported mesh) to .ply",
    )
    parser.add_argument(
        "input_path",
        type = Path,
        help = "Path to the input mesh file",
        )
    parser.add_argument(
        "-o",
        "--out",
        type = Path,
        default = None,
        help = "Path where the output needs to be saved (with file name and suffix)"
    )

    console = Console()


    console.print("[bold]mesh-to-ply[/bold]")

    args = parser.parse_args()
    out_path = args.out if args.out else args.input_path.with_suffix(".ply")

    with console.status("[cyan]Converting to .ply..."):
        convert(args.input_path, out_path)

    console.print(f"[green]✔ Converting to .ply complete[/green]")

    try:
        rel = out_path.relative_to(Path.cwd())
    except ValueError:
        rel = out_path  # fallback to absolute path
    console.print(f"Wrote: {rel}")

if __name__ == "__main__":
    main()