"""Safe DBSARE CLI foundation."""
import argparse, json
from .core import DBSARECore

def main() -> int:
    parser=argparse.ArgumentParser(prog="dbsare")
    sub=parser.add_subparsers(dest="command")
    sub.add_parser("status")
    sub.add_parser("brain")
    sub.add_parser("evidence")
    sub.add_parser("investigate")
    sub.add_parser("health")
    args=parser.parse_args()
    core=DBSARECore()
    if args.command=="status": print(core.status())
    elif args.command=="brain": print(core.brain.summary())
    elif args.command=="evidence": print(core.evidence.summary())
    elif args.command=="investigate": print(core.investigation.summary())
    elif args.command=="health":
        from .health import report
        print(json.dumps(report(), indent=2))
    else: parser.print_help()
    return 0

if __name__=="__main__":
    raise SystemExit(main())
