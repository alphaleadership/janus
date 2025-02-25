import sys
import time
import logging
import torch
from model import JanusPipeline
import os
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
nombre_fichiers = len(os.listdir('./tmp'))
log.info(f'Nombre de fichiers dans le dossier tmp: {nombre_fichiers}')

repo_id = 'deepseek-ai/Janus-1.3B'
#repo_id = 'deepseek-ai/Janus-Pro-7B'
cache_dir = '/mnt/models/huggingface'

 


    
def gen(prompt):
        log.info(f'prompt={prompt}')
        t0 = time.time()
        pipe = JanusPipeline(
            repo_id,
            cache_dir=cache_dir,
            dtype=torch.bfloat16,
            device='auto',
        )
        t1 = time.time()
        log.info(f'load time={t1-t0}')
        images = pipe(
                prompt=prompt,
            num_images_per_prompt=10,
            temperature=1.0,
            guidance_scale=1.0,
        )
        t2 = time.time()
        log.info(f'generate time={t2-t1}')
        for i, image in enumerate(images):
            
            fn = f'./tmp/janus-{i+nombre_fichiers}.png'
            log.info(f'image={i} file={fn}')
            image.save(fn)
gen("quand tu quitte ton post tu le verrouille")
