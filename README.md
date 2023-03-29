# TEORÍA DE SUMA DE FOURIER
La suma de Fourier es una técnica matemática que permite aproximar cualquier función periódica mediante una serie de senos y cosenos. Esta técnica se utiliza principalmente en el análisis de señales y en la teoría de la comunicación, y es especialmente útil para el procesamiento de señales digitales.

La idea detrás de la suma de Fourier es que cualquier función periódica puede expresarse como una suma infinita de senos y cosenos de diferentes frecuencias y amplitudes. Estos senos y cosenos se denominan armónicos, y la suma de todos ellos se conoce como serie de Fourier.

En términos prácticos, la suma de Fourier se utiliza para descomponer una señal compleja en sus componentes fundamentales de frecuencia. Esta descomposición puede ser útil para analizar y entender la señal, y también para procesarla de diferentes formas. Por ejemplo, es posible filtrar la señal para eliminar frecuencias no deseadas, o para enfatizar ciertas frecuencias importantes.

En resumen, la suma de Fourier es una herramienta matemática poderosa que se utiliza en el análisis y procesamiento de señales. Permite aproximar cualquier función periódica mediante una serie de senos y cosenos, y puede ser muy útil para entender y manipular señales complejas.

# FÓRMULA
La fórmula de la suma de Fourier es la siguiente:

f(x) = a0/2 + Σ(ancos(nωx) + bnsin(nωx)), donde:

* f(x) es la función periódica que se quiere aproximar.
* a0 es el coeficiente de la componente DC, que representa el valor medio de la función.
* an y bn son los coeficientes de las componentes armónicas, que representan la amplitud de cada seno y coseno de la serie.
* ω es la frecuencia angular fundamental de la señal, que se calcula como 2π/T, donde T es el período de la señal.
* n es el número de la componente armónica, que puede ser cualquier número entero positivo.

La suma de Fourier se representa como una serie infinita, que incluye términos para todas las frecuencias armónicas posibles. En la práctica, es necesario truncar la serie a un número finito de términos para obtener una aproximación útil de la función original. El número de términos necesarios depende de la complejidad de la función y de la precisión requerida en la aproximación.

# EJEMPLOS

## EJEMPLO 1

En este ejemplo, se define una señal periódica como una suma de tres senos de diferentes frecuencias. Luego se calculan los coeficientes de Fourier utilizando la integración numérica, y se usa la serie de Fourier truncada a 20 términos para aproximar la señal original. Finalmente, se grafican ambas señales para comparar la aproximación con la señal original.

![image](https://user-images.githubusercontent.com/91994346/228426861-e96a6b68-5df7-4cf2-9fd4-e456fa771396.png)

## EJEMPLO 2

En este ejemplo, se define una función fourier_series_coeff que toma una función f y calcula los coeficientes de la serie de Fourier utilizando la fórmula que mencioné en la respuesta anterior. Luego se define la función f que queremos descomponer (en este caso, una función sinusoide con una frecuencia tres veces mayor). Se llama a la función fourier_series_coeff para calcular los coeficientes de la serie de Fourier, y se utiliza una suma de términos sinusoidales para aproximar la función original utilizando la serie de Fourier. Finalmente, se grafican la función original y su aproximación por la serie de Fourier.

![image](https://user-images.githubusercontent.com/91994346/228427655-012cc6c6-9bd5-44d9-9ed7-73174858fcd7.png)

