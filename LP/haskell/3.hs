imprime :: Int -> IO ()
imprime n = print (take n [1,3..])

main :: IO ()
main = do
  putStrLn "insira um numero:"
  n <- readLn
  imprime n
