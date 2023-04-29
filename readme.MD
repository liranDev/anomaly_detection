train wgan
```bash
python3 train_wgangp.py --train_root dataset/train --seed 222 --n_epochs 100
```


train encoder
```bash
python train_encoder_izif.py --train_root dataset/train --seed 222 --n_epochs 100
```

test \ validation

```bash
# validation
python test_anomaly_detection.py --test_root dataset/val/

# test
python test_anomaly_detection.py --test_root dataset/test/
```

save results
```bash
python save_compared_images.py --test_root dataset/test/ --n_iters 0 --n_grid_lines 10
```