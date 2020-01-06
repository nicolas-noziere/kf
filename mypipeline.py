import kfp.dsl as dsl


@dsl.pipeline(
  name='1step',
  description='this is my first step'
)
def train_and_deploy():
  """Pipeline to train babyweight model"""
  preprocess = dsl.ContainerOp(
      name='preprocess',
      # image needs to be a compile-time string
      image='gcr.io/mysandbox-253109/hello-world-tf:0.1',
      file_outputs={'bucket': '/output.txt'}
    )



if __name__ == '__main__':
  import kfp.compiler as compiler
  compiler.Compiler().compile(train_and_deploy, './mypipeline.tar.gz')
