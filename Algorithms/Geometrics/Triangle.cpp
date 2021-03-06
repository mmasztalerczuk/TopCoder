class fPoint
{
public:
    int x;
    int y;
 
};
 
float sign (fPoint p1, fPoint p2, fPoint p3)
{
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}
 
bool PointInTriangle (fPoint pt, fPoint v1, fPoint v2, fPoint v3)
{
    bool b1, b2, b3;
 
    b1 = sign(pt, v1, v2) < 0.0f;
    b2 = sign(pt, v2, v3) < 0.0f;
    b3 = sign(pt, v3, v1) < 0.0f;
 
    return ((b1 == b2) && (b2 == b3));
}
