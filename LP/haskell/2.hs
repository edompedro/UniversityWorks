main :: IO ()

primo :: Int -> Bool
primo n
  | n <= 1    = False
  | otherwise = null [x | x <- [2..isqrt n], n `mod` x == 0]    --gera uma lista de 2 até a raiz do numero
                                                                --e ve se o numero é divisivel, se não for retorna true
  where
    isqrt = floor . sqrt . fromIntegral
    
main = return ()