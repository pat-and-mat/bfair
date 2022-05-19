import subprocess
import sys
from pathlib import Path


def explode(args, index=0, current=(), highlights=()):
    if index >= len(args):
        yield current, highlights
    else:
        components = args[index].split("|")
        for c in components:
            yield from explode(
                args,
                index + 1,
                current + (c,),
                highlights if len(components) < 2 else highlights + (c,),
            )


def run(cmd):
    process = subprocess.Popen(
        cmd,
        universal_newlines=True,
        stderr=subprocess.PIPE,
    )
    process.wait()
    if process.returncode:
        raise Exception(process.stderr.read())


def main(name, output_dir, *args):
    output_dir = Path(output_dir)
    if not output_dir.is_dir():
        raise ValueError(f"Invalid output dir: {output_dir}")

    report_path = output_dir / "__report__.txt"
    output_stream = report_path.open(mode="w")

    for options, highlights in explode(args):
        output_path = output_dir / f"{name}[{{}}].{'.'.join(highlights)}.txt"

        cmd = [
            "python",
            "-m",
            f"experiments.{name}",
            "--output",
            str(output_path),
            "--title",
            repr(".".join(highlights)),
        ]
        cmd.extend(options)

        textual_cmd = " ".join(cmd)
        print("============", file=output_stream)
        print("- STARTING -", file=output_stream)
        print("============", file=output_stream)
        print(textual_cmd, file=output_stream)
        print("------------", file=output_stream, flush=True)
        try:
            run(cmd)
            print("DONE!", file=output_stream)
        except Exception as e:
            print("", file=output_stream)
            print(e, file=output_stream)
            print("ERROR!", file=output_stream)
        print("============", file=output_stream)
        print("\n", file=output_stream, flush=True)

        output_path.with_suffix(".sh").write_text(textual_cmd)

    output_stream.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python -m experiments <name> <output-dir> *<args>")
        print("- Arguments including `|` will be splitted.")
    else:
        main(*sys.argv[1:])
