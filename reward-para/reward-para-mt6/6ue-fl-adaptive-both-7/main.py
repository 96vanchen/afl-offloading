


from runner import Runner
from common.arguments import get_args
from common.utils import make_env
import numpy as np
import random
import torch
import runner


if __name__ == '__main__':
    # get the params
    args = get_args()
    map_mec, args = make_env(args)
    runner = Runner(args, map_mec)
    if args.evaluate:
        returns = runner.evaluate()
        print('Average returns is', returns)
    else:
        runner.run()
