using UnityEngine;

public class Z_Slide : MonoBehaviour
{
    public ZSlide_Ctrl ctrl;

    [Header("Individual Components")]
    public GameObject Carriage;
    public GameObject Pivot;
    public GameObject Sensors;

    [Header("Full Assembly Root Object")]
    public GameObject Complete;

    // Movement along the world Z-axis
    private readonly Vector3 ZDirection = Vector3.forward;

    void FixedUpdate()
    {
        float translation = ctrl.speed * Time.fixedDeltaTime;
        if (ctrl.Forward && !ctrl.Stop)
        {
            ctrl.Backward = false;
            Complete.transform.Translate(ZDirection * translation, Space.World);
        }
        else if (ctrl.Backward && !ctrl.Stop)
        {
            ctrl.Forward = false;
            Complete.transform.Translate(-ZDirection * translation, Space.World);
        }
        if (ctrl.Stop)
        {
            ctrl.Forward = false;
            ctrl.Backward = false;
        }
        Debug.DrawRay(Complete.transform.position, ZDirection * 2, Color.green);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("UpSW"))
        {
            Debug.Log("Upper switch hit");
            ctrl.Forward = false;
            ctrl.Stop = true;
        }
        if (other.CompareTag("DownSW"))
        {
            Debug.Log("Lower switch hit");
            ctrl.Backward = false;
            ctrl.Stop = true;
        }
    }
}
