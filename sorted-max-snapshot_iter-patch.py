# coding: utf-8


# This is a patch for failure to get maximum number snapshot (latest snapshot)
#
# Example:  list are
#   snapshot_iter_9000
#   snapshot_iter_10000
#
#   and sorted the list, output order is snapshot_iter_10000 snapshot_iter_9000 (maybe first digit 9 is bigger than 1)
#   then sorted list[-1] becomes snapshot_iter_9000, it's not latest one.

'''
out_dir = './drive/wavenet/result'  # Directory to output the result

(以前に学習させてその途中結果がsnapshotとして、./drive/wavenet/result/以下に保存されています。
そこから再開させるためのコードです。はじめての場合に実行しても、特に何も起きません。)
'''

import glob

# Resume latest snapshot if exists

model_files = sorted(glob.glob(out_dir + '/snapshot_iter_*'))

if len(model_files) > 0:
    resume = [x for x in model_files if len(x)== len(max(model_files, key=len))] [-1] # <--- change
    print('model: {}'.format(resume))
    # chainer.serializers.load_npz(resume, trainer)
