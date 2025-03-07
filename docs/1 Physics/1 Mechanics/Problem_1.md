# Problem 1
Investigating the Range as a Function of the Angle of Projection

how the range of a projectile depends on its angle of projection.
lets start from what is range of projection and what is angle of projection.

range of projection is the distance that a projectile has to travel before it hits the ground.
the range can be horisontal or vertical.
angle of projection is the angle of which the projectile is projected from the ground. 
in other words we have a projectile that "shoots" from a point at a certain angle.
 
 how range depends on angle
 vertical
 if the angle is small the vertical range is also small which means the projectile will return(hit) to the ground faster. 
 if the angle is big the vertical range is big which means the projectile will go far vertically before it hits the ground.
 horisontal
if the angle is small the horisontal range is big which means the projectile will go far horisontally before it hits the ground.
if the angle is big the horisontal range is small which means the projectile will return(hit) to the ground faster.

the eqations:
horisontal motion is $x=v_0cos(θ)t$
vertical motiion is $y=v_0sin(θ)t-\frac{1}{2}gt^2$
and range is $R=\frac{v_0^2sin(2θ)}{g}$
$v_0$ is the velocity, 
$θ$ is the angle of projection, 
$g$ is the acceleration due to gravity.

[Angle to range in geogebra](https://www.geogebra.org/calculator/jubc9rkb)

from this we can confirm that 
if $v_0<θ$ than the range is smaller than if $v_0>θ$.

45 gives max range, lets prove this 
we can prove it with trugonometry and caclculus

trigonometry

sin's function is maximum when the angle is 90°
and from the equation of range 
$R=\frac{v_0^2sin(2θ)}{g}$
we can see that max angle is $sin(2θ)=90$
$2θ=90$
$θ=45$

this can also be proven with calculus, from the formula
$R=\frac{v_0^2sin(2θ)}{g}$
we want to maximize the range(R) so we need to find the maximum of the function
how to find the maximum of the function:
we need to find the derivative of the function and set it to 0
we specifficaly want to find the derivative of $θ$
so after differnciating R with respect to $θ$ we get
$\frac{dR}{dθ}=\frac{2v_0^2}{g}cos(2θ)$
now we need to set it to 0
$\frac{2v_0^2}{g}cos(2θ)=0$
we know that $v_0^2$ and $g$ are constants so we can ignore them
$cos(2θ)=0$
maximum angle of $θ$ is $90°$ so
$2θ=90$
$θ=45$

this proves that 45° gives the maximum range using calculus.

how increasing velocity increases range
from the equation of range we see that range is proportional to the square of the velocity
 



How increasing velocity increases range.
Ideas for future improvements (air resistance, wind, etc.).